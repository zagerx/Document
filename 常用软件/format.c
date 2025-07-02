void test_fun(void)
{
  int a = 0;
  if(a) {}
}
int main(void)
{
  void *p = NULL;
  int a = 0;
  test_fun();
  if(a != 1) {
    p = (void *)&a;
  } else if(a == 1) {
    p = (void *)&a;
  } else {
    a = 2;
  }
  return 1;
}