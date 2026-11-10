#!/usr/bin/env python3
"""Regression tests for the existing CS schema and the BKT additions."""

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.dont_write_bytecode = True
from validate_submission import BKT_ARTIFACT_FILES, validate_folder


class ValidateSubmissionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def make_submission(self, slug="may_day_sprint", bkt=True):
        folder = self.root / f"{slug}_nhom01"
        folder.mkdir()
        (folder / "submission.json").write_text(
            json.dumps({
                "case_study_slug": slug,
                "case_study_id": "BKT-1" if bkt else "CS-1",
                "group_code": "nhom01",
                "members": ["12345678"],
                "scenario": "khong_ap_dung",
                "submitted_at": "2026-11-02",
            }), encoding="utf-8"
        )
        (folder / "README.md").write_text("Bai lam mau de kiem thu.\n", encoding="utf-8")
        if bkt:
            (folder / "source-ref.json").write_text(
                json.dumps({
                    "starter_repo": "https://example.org/starter",
                    "starter_commit": "a" * 40,
                    "fork_url": "https://example.org/fork",
                    "final_commit": "b" * 40,
                    "release_tag": "bkt-2026-nhom01-rc1",
                    "ci_run_url": "https://example.org/runs/1",
                }), encoding="utf-8"
            )
            artifacts = folder / "artifacts"
            artifacts.mkdir()
            for name in BKT_ARTIFACT_FILES:
                (artifacts / name).write_text("Noi dung kiem thu.\n", encoding="utf-8")
        return folder

    def test_existing_cs_passes_without_bkt_files(self):
        self.assertEqual(validate_folder(self.make_submission("may_day", bkt=False)), [])

    def test_complete_ruleengine_bkt_passes(self):
        self.assertEqual(validate_folder(self.make_submission()), [])

    def test_complete_vuontoan_bkt_passes(self):
        self.assertEqual(validate_folder(self.make_submission("hoang_mai_toan")), [])

    def test_missing_artifacts_fails(self):
        folder = self.make_submission()
        for file in (folder / "artifacts").iterdir():
            file.unlink()
        (folder / "artifacts").rmdir()
        self.assertTrue(any("artifacts/" in error for error in validate_folder(folder)))

    def test_source_ref_template_placeholder_fails(self):
        folder = self.make_submission()
        path = folder / "source-ref.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["ci_run_url"] = "REPLACE_VOI_CI_RUN_URL"
        path.write_text(json.dumps(data), encoding="utf-8")
        self.assertTrue(any("ci_run_url" in e and "giá trị mẫu" in e for e in validate_folder(folder)))

    def test_submission_bkt_template_id_fails(self):
        folder = self.make_submission()
        path = folder / "submission.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["case_study_id"] = "REPLACE_VOI_MA_BKT"
        path.write_text(json.dumps(data), encoding="utf-8")
        self.assertTrue(any("case_study_id" in e for e in validate_folder(folder)))

    def test_missing_source_ref_fails(self):
        folder = self.make_submission()
        (folder / "source-ref.json").unlink()
        self.assertTrue(any("source-ref.json" in error for error in validate_folder(folder)))

    def test_missing_source_ref_field_fails(self):
        folder = self.make_submission()
        source_ref_path = folder / "source-ref.json"
        source_ref = json.loads(source_ref_path.read_text(encoding="utf-8"))
        del source_ref["ci_run_url"]
        source_ref_path.write_text(json.dumps(source_ref), encoding="utf-8")
        self.assertTrue(any("ci_run_url" in error for error in validate_folder(folder)))

    def test_empty_source_ref_field_fails(self):
        folder = self.make_submission()
        source_ref_path = folder / "source-ref.json"
        source_ref = json.loads(source_ref_path.read_text(encoding="utf-8"))
        source_ref["ci_run_url"] = "   "
        source_ref_path.write_text(json.dumps(source_ref), encoding="utf-8")
        self.assertTrue(any("ci_run_url" in error for error in validate_folder(folder)))

    def test_invalid_source_ref_json_fails(self):
        folder = self.make_submission()
        (folder / "source-ref.json").write_text("{invalid", encoding="utf-8")
        self.assertTrue(any("source-ref.json" in error and "JSON" in error
                            for error in validate_folder(folder)))

    def test_empty_artifact_fails(self):
        folder = self.make_submission()
        (folder / "artifacts" / "AI_USE.md").write_bytes(b"")
        self.assertTrue(any("artifacts/AI_USE.md" in error and "rỗng" in error
                            for error in validate_folder(folder)))

    def test_invalid_slug_fails(self):
        self.assertTrue(any("case_study_slug" in error and "không hợp lệ" in error
                            for error in validate_folder(self.make_submission("abc", bkt=False))))

    def test_bkt_template_cannot_be_submitted(self):
        folder = self.root / "_TEMPLATE_BKT_RULEENGINE"
        folder.mkdir()
        self.assertTrue(any("thư mục mẫu" in error for error in validate_folder(folder)))


if __name__ == "__main__":
    unittest.main()
