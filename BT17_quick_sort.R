# Quick Sort
quick_sort<-function(x)
{
  if(length(x)<=1) return(x)
  i<-x[1]
  j<-x[-1]
  i_less<-quick_sort(j[j<i])
  i_greater<-quick_sort(j[j>=i])
  return(c(i_less,i,i_greater))
}


quick_sort(c(5,4,12,13,45, 3,8,85))
