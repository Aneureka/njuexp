//
// Created by Hiki on 2017/5/27.
// 一些定义宏
//

#ifndef MEMORY_MANAGEMENT_PROP_H
#define MEMORY_MANAGEMENT_PROP_H

#define INT_BYTE 4
#define CHAR_BYTE 1
#define INT_SIZE 32
#define CHAR_SIZE 8

#define PPI_SIZE INT_BYTE
#define PAGE_SIZE (1024 * 8)
#define MAX_V_PAGE_NUM (((1024 * 1024 * 128) + (1024 * 1024 * 512)) / PAGE_SIZE)
#define MAX_P_PAGE_NUM (((1024 * 1024 * 128) + (1024 * 1024 * 512)) / PAGE_SIZE)
#define MAX_PM_PAGE_NUM ((1024 * 1024 * 128) / PAGE_SIZE)

#define MAX_PROCESS_NUM 1024
#define MAX_ALLOC_TIME 100
#define ALLOC_SIZE (INT_BYTE + INT_BYTE)
#define PROC_SIZE (ALLOC_SIZE * MAX_ALLOC_TIME)

#define START_VPI_PA 0
#define START_PPI_PA (MAX_V_PAGE_NUM * INT_BYTE)
#define START_PROC_PA (MAX_V_PAGE_NUM * INT_BYTE + MAX_P_PAGE_NUM * CHAR_BYTE)
#define START_PI ((MAX_V_PAGE_NUM * INT_BYTE + MAX_P_PAGE_NUM * CHAR_BYTE + MAX_PROCESS_NUM * PROC_SIZE) / PAGE_SIZE)

#define EMPTY 0

#endif //MEMORY_MANAGEMENT_PROP_H
