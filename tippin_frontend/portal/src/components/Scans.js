import React, { useState } from "react";
import ListGroup from "react-bootstrap/ListGroup";
import Scan from "./Scan";

const Scans = () => {
  const [cardData, setCardData] = useState([
    {
      id: "123",
      imgSrc: "https://unsplash.com/photos/Vc2dD4l57og",
      title: "test",
      text: "trying",
    },
    {
      id: "123",
      imgSrc: "https://unsplash.com/photos/Vc2dD4l57og",
      title: "test",
      text: "trying",
    },
    {
      id: "123",
      imgSrc: "https://unsplash.com/photos/Vc2dD4l57og",
      title: "test",
      text: "trying",
    },
  ]);

  return (
    <ListGroup>
      {cardData.map((card, index) => (
        <ListGroup.Item key={index} className="my-1">
          <Scan
            key={card.id}
            imgSrc={card.imgSrc}
            title={card.title}
            text={card.text}
          />
        </ListGroup.Item>
      ))}
    </ListGroup>
  );
};

export default Scans;
