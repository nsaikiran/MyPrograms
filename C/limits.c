/*
This program is to enquire the mazximimum and minimum values of INTEGRAL types ; they are system dependent.
by saikiran638															
*/

# include <stdio.h>
# include <limits.h>

int main(void){
	printf("CHAR_BIT\t:%d\nCHAR_MAX\t:%d\nUCHAR_MAX\t:%d\nSCHAR_MAX\t:%d\n"
	"CHAR_MIN\t:%d\nSCHAR_MIN\t:%d\nINT_MAX\t\t:%d\nINT_MIN\t\t:%d\nLONG_MAX\t:%ld\n"
	"LONG_MIN\t:%ld\nSCHAR_MAX\t:%d\nSCHAR_MIN\t:%d\nSHRT_MAX\t:%d\nSHRT_MIN\t:%d\nUCHAR_MAX\t:%d\n"
	"UINT_MAX\t:%u\nULONG_MAX\t:%lu\nUSHRT_MAX\t:%u\nLLONG_MAX\t:%lld\n"
	"LLONG_MIN\t:%lld\nULLONG_MAX\t:%llu\n"
	"\nSIZEs in bytes\nsizeof char\t:%lu\nsizeof short\t:%lu\nsizeof int\t:%lu\nsizeof long\t:%lu\nsizeof long long:%lu\n",
	CHAR_BIT,
	CHAR_MAX ,
	UCHAR_MAX,
	 SCHAR_MAX,
	CHAR_MIN,
	SCHAR_MIN,
	INT_MAX,
	INT_MIN,
	LONG_MAX,
	LONG_MIN,
	SCHAR_MAX,
	SCHAR_MIN,
	SHRT_MAX,
	SHRT_MIN,
	UCHAR_MAX,
	UINT_MAX,
	ULONG_MAX,
	USHRT_MAX,
	LLONG_MAX,
	LLONG_MIN,
	ULLONG_MAX,
	sizeof(char),
	sizeof(short),
	sizeof(int),
	sizeof(long),
	sizeof(long long)
	);
	return 0;
	}
