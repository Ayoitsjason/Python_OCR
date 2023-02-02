import axios from "axios";

const BACKEND_URL = "http://127.0.0.1:8000";

export const scanFile = async (form) => {
  const formData = new FormData(form);

  try {
    let res = await axios.post(`${BACKEND_URL}/payroll/scan`, formData);
    console.log(res);
  } catch (err) {
    console.error(err);
  }
};
