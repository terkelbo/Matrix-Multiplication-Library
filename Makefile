TARGET	= libmatmult.so

SRC_DIR = src
OBJ_DIR = obj

SRC = $(wildcard $(SRC_DIR)/*.c)
OBJ = $(SRC:$(SRC_DIR)/%.c=$(OBJ_DIR)/%.o)

CPPFLAGS = -Iinclude

LIBSRCS	= matmult_nat.c matmult_lib.c matmult_mnk.c matmult_nmk.c matmult_nkm.c matmult_knm.c matmult_mkn.c matmult_kmn.c matmult_blk.c
LIBOBJS	= matmult_nat.o matmult_lib.o matmult_mnk.o matmult_nmk.o matmult_nkm.o matmult_knm.o matmult_mkn.o matmult_kmn.o matmult_blk.o

OPT	= -g -Ofast -funroll-loops
PIC	= -fPIC

CC	= gcc
CFLAGS= $(OPT) $(PIC) $(XOPTS) 

SOFLAGS = -shared 
XLIBS	= -L /usr/lib64/atlas -lsatlas

$(TARGET): $(OBJ)
	$(CC) -o $@ $(SOFLAGS) $(OBJ) $(XLIBS) 

$(OBJ_DIR)/%.o: $(SRC_DIR)/%.c
	$(CC) $(CPPFLAGS) $(CFLAGS) -c $< -o $@

clean:
	@/bin/rm -f core core.* $(OBJ_DIR)/$(OBJ) 

#matmult_nat.o: matmult_nat.c matmult_nat.h
#matmult_lib.o: matmult_lib.c matmult_lib.h
#matmult_mnk.o: matmult_mnk.c matmult_mnk.h
#matmult_nmk.o: matmult_nmk.c matmult_nmk.h
#matmult_nkm.o: matmult_nkm.c matmult_nkm.h
#matmult_knm.o: matmult_knm.c matmult_knm.h
#matmult_mkn.o: matmult_mkn.c matmult_mkn.h
#matmult_kmn.o: matmult_kmn.c matmult_kmn.h
#matmult_blk.o: matmult_blk.c matmult_blk.h
# DO NOT DELETE
