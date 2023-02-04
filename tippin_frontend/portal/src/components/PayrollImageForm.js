import React, { useContext, useState } from "react";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";
import Alert from "react-bootstrap/Alert";
import Spinner from "react-bootstrap/Spinner";
import { MyTexts } from "../contexts/texts";
import { scanFile } from "../api/PayrollService";

function FileUploadForm() {
  const [file, setFile] = useState(null);
  const [success, setSuccess] = useState(false);
  const [failed, setFailed] = useState(false);
  const [loading, setLoading] = useState(false);
  const { texts, setTexts } = useContext(MyTexts);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    setLoading(true);
    const promise = scanFile(e.target);
    promise
      .then((res) => {
        setSuccess(true);
        setTexts([...texts, res.data]);
      })
      .catch((err) => {
        setFailed(true);
        console.error(err);
      });
    setTimeout(() => {
      setLoading(false);
      setSuccess(false);
      setFailed(false);
    }, 1000);
  };

  return (
    <>
      {success && (
        <Alert key={`success`} variant={`success`}>
          Successfully Scanned
        </Alert>
      )}
      {failed && (
        <Alert key={`danger`} variant={`danger`}>
          Failed To Scan
        </Alert>
      )}
      <Form onSubmit={handleSubmit}>
        <Row className="mb-3">
          <Form.Group as={Col} controlId="file">
            <Form.Label>Upload Photo</Form.Label>
            <Form.Control name="file" type="file" onChange={handleFileChange} />
          </Form.Group>
          <Form.Group as={Col}>
            <Form.Label>Text Format?</Form.Label>
            <Form.Select name="format">
              <option>Row Text</option>
              <option>Column Text</option>
              <option>Block Text</option>
              <option>Single Text Line</option>
              <option>Single Word</option>
            </Form.Select>
          </Form.Group>
        </Row>
        <Row className="mb-3">
          <Form.Text className="text-muted">
            Get text from your photo.
          </Form.Text>
        </Row>
        <Button variant="primary" type="submit">
          {loading ? (
            <Spinner animation="border" variant="light" size="sm" />
          ) : (
            `Upload`
          )}
        </Button>
      </Form>
    </>
  );
}

export default FileUploadForm;
