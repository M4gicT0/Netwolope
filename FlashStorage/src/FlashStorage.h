#ifndef FLASH_STORAGE_H
#define FLASH_STORAGE_H

typedef enum {
  FS_ERR_UNKNOWN = 10,
  FS_ERR_ERASE_FAILED,
  FS_ERR_WRITE_FAILED,
  FS_ERR_READ_FAILED,
  FS_ERR_INVALID_STATE
} FlashStorageError;

#endif /* FLASH_STORAGE_H */
