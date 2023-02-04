import React, { createContext, useState } from "react";

export const MyTexts = createContext();

export function TextProvider(props) {
  const [texts, setTexts] = useState([]);

  return (
    <MyTexts.Provider value={{ texts, setTexts }}>
      {props.children}
    </MyTexts.Provider>
  );
}
