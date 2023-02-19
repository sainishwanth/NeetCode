#include<stdio.h>
#include<stdlib.h>

int* productExceptSelf(int* nums, int numsSize, int* returnSize){
    int sum = 1;
    int sum2 = 1;
    int count = 0;
    int n = numsSize;
    for(int i = 0; i < n; ++i){
        sum *= nums[i];
        if(i != 0){
            sum2 *= nums[i];
        }else{
            count += 1;
        }
    }
    int *nums2 = malloc(n * sizeof(int));
    for(int i = 0; i < n; ++i){
        if(i == 0){
            if(count == 1){
                nums2[i] = sum2;
                continue;
            }else{
                nums2[i] = 0;
                continue;
            }
        }
        nums2[i] = sum/i;
    }
    return nums2;
}
