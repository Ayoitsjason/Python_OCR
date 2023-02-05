import axios from "axios";

export const scanFile = async (form) => {
  const formData = new FormData(form);
  try {
    const config = {
      headers: {
        "content-type": "multipart/form-data",
      },
    };
    let res = await axios.post(
      `${process.env.REACT_APP_BACKEND_URL}/payroll/scan`,
      formData,
      config
    );
    return res;
  } catch (err) {
    console.error(err);
    throw err;
  }
};
