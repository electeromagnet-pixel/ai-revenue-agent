# APEX original offline TIFF document-renaming sample

State: researched / locally tested / review-only. This is NOT a funded customer assignment, an accepted delivery, a live deployed service, or a verified revenue source. A November 17, 2026 marketplace posting advertised a $100 document automation budget, but the job was NOT applied to and the applicant identity gate is unresolved.

## Workflow

A local Tesseract OCR executable reads TIFF files; the operator supplies a regex with exactly one capture group defining the authoritative identifier. The program previews in-place filename changes. Example:

    python examples/tiff_ocr_batch/batch_tiff_renamer.py /path/to/scans --pattern 'INVOICE:\s+([A-Z0-9-]+)' --manifest preview.csv

After checking the preview and backing up inputs, add --apply --manifest executed.csv. No OCR text is transmitted over the network or persisted in the manifest. Symlinks, collisions, unmatched labels, unsafe names and existing targets never get silently overwritten. On the same filesystem, exclusive hardlink creation precedes unlinking the source; a partial failure may leave two copies but does not overwrite existing files. Blocked entries prevent apply.

Python code uses only the standard library; OCR requires a separately installed licensed Tesseract executable and language pack. Default safety limits are 1,000 input TIFFs and 20 seconds OCR per file. These are not throughput benchmarks.

## Evidence and boundaries

Nine stdlib unit tests passed locally Nov 17. A synthetic end-to-end TIFF displaying "INVOICE: DEMO-2046" passed OCR, dry run, then explicit apply. No client data, buyer contact, payment, remote service, account or purchase was used. Large batches, handwriting, low-quality scans, actual buyer field grammar, support resources and privacy permission are unverified. Do not submit Upwork proposals or spend Connects while identity/approval gates remain unresolved. This is preparation, not paid-client experience.
