import React, { useState } from "react";
import { uploadEtf } from "../services/api";

interface FileUploadProps {
  onUploadSuccess: () => void;
}

const FileUpload: React.FC<FileUploadProps> = ({ onUploadSuccess }) => {
  const [file, setFile] = useState<File | null>(null);
  const [uploading, setUploading] = useState(false);

  const handleFileChange = (e: any) => {
    if (e.target.files && e.target.files[0]) {
      setFile(e.target.files[0]);
    }
  };

  const handleUploadFile = async () => {
    if (!file) {
      alert("Please select a file first");
      return;
    }

    setUploading(true);
    try {
      await uploadEtf(file);
      onUploadSuccess();
    } catch (error) {
      console.error("Error uploading ETF:", error);
      alert("Failed to upload ETF");
    } finally {
      setUploading(false);
    }
  };

  return (
    <div className="d-flex align-items-center gap-3">
      <input
        type="file"
        accept=".csv"
        onChange={handleFileChange}
        className="form-control form-control-sm"
        style={{ maxWidth: "300px" }}
      />
      <button className="btn btn-primary" onClick={handleUploadFile}>
        {uploading ? (
          <>
            <span
              className="spinner-border spinner-border-sm me-2"
              role="status"
              aria-hidden="true"
            ></span>
            Uploading...
          </>
        ) : (
          "Upload Data"
        )}
      </button>
    </div>
  );
};

export default FileUpload;
