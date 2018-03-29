#include "PCComm.h"

interface PCConnection {
  
  /**
   * Initiate a communication line with the PC.
   * The <code>established</code> will be signaled when a 
   * connection is successfully established.
   */
  command void init();
  
  /**
   * Attempts to send partial data to the PC.
   * 
   * @param data  A pointer to a buffer
   * @param size  The length of data to send.
   */
  command void send(uint8_t* data, uint8_t size);
  
  /**
   * Signaled when a connection to the PC is established successfully.
   */
  event void established();
  
  /**
   * Signaled when a communication error occurs.
   * 
   * @param error The error code describing the error.
   */
  event void error(PcCommunicationError error);
  
  /**
   * Signaled when some data has been sent successfully.
   */
  event void sent();
}