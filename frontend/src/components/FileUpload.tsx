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
    <div>
      <h2>Upload ETF CSV</h2>
      <input type="file" accept=".csv" onChange={handleFileChange} />
      <button onClick={handleUploadFile} disabled={uploading}>
        {uploading ? "Uploading..." : "Upload"}
      </button>
    </div>
  );
};

export default FileUpload;
