# S???p x???p ch???n
selection_sort <- function(x) {
  n <- length(x)
  for (i in 1:(n-1)) {
    for(j in (i+1)) {
      if(x[j]<x[i]){
        temp <- x[i]
        x[i] <- x[j]
        x[j] <- temp
      }
    }
  }
  return(x)}
# Ki???u d??? quy
selfsort <- function(x){
  if(length(x)>1){
    min <- which.min(x)
    c(x[min], selfsort(
      x[-min]))
  }else x
}

