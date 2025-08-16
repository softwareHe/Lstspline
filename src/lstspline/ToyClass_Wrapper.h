#ifndef TOYCLASS_WRAPPER_H
#define TOYCLASS_WRAPPER_H

#ifdef __cplusplus
extern "C" {
#endif

typedef void* ToyClassHandle;
typedef void* StatsClassHandle;


ToyClassHandle ToyClass_create(int size);
void ToyClass_destroy(ToyClassHandle obj);
void ToyClass_set_value(ToyClassHandle obj, int index, double value);
double ToyClass_get_value(ToyClassHandle obj, int index);
double ToyClass_sum(ToyClassHandle obj);
int SIZE(ToyClassHandle obj); 

StatsClassHandle StatsClass_create(ToyClassHandle toyHandle);
void StatsClass_destroy(StatsClassHandle handle);
double StatsClass_mean(StatsClassHandle handle);
double StatsClass_median(StatsClassHandle handle);
double StatsClass_mode(StatsClassHandle handle);

#ifdef __cplusplus
}
#endif

#endif // TOYCLASS_WRAPPER_H
