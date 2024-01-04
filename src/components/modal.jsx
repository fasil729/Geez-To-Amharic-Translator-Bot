import React, { useState } from 'react';
import { Modal, Button } from 'react-bootstrap';

const MyModal = ({children,title,label,data}) => {
  const [showModal, setShowModal] = useState(false);

  const closeModal = () => {
    // Implement your text condition here
     // Replace with your actual text condition check

    // If the text condition is true, close the modal
    if (data===" ") {
      setShowModal(true);
    }
    else{
      setShowModal(false);
    }
  };

  return (
    <>{data===" "&&<div className='container'>
    <button className='btn btn-none' onClick={()=>closeModal()}>{label}</button>
    <Modal show={showModal} onHide={closeModal}>
      <Modal.Header closeButton>
        <Modal.Title>{title}</Modal.Title>
      </Modal.Header>
      <Modal.Body>
        {/* Your modal content */}
       {children}
      </Modal.Body>
      <Modal.Footer>
        <Button variant="secondary" onClick={closeModal}>
         Close
        </Button>
      </Modal.Footer>
    </Modal>
  </div>}</>
  );
};

export default MyModal;
