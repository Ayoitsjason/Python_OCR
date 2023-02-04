import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";
import React from "react";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import Main from "./components/Main";
import Scans from "./components/Scans";
import PayrollImageForm from "./components/PayrollImageForm.js";
import { TextProvider } from "./contexts/texts";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Main />,
    children: [
      {
        path: "/",
        element: (
          <TextProvider>
            <PayrollImageForm />
          </TextProvider>
        ),
      },
      {
        path: "history",
        element: (
          <TextProvider>
            <Scans />
          </TextProvider>
        ),
      },
    ],
  },
]);

function App() {
  return <RouterProvider router={router} />;
}

export default App;
