# S???p x???p n???i b???t(Bubble_Sort) 
Bubble_sort <- function(x){
  n<-length(x)
  for(j in 1:(n-1)){
    for(i in 1:(n-j)){
      if(x[i]>x[i+1]){
        temp<-x[i]
        x[i]<-x[i+1]
        x[i+1]<-temp
      }
    }
  }
  return(x)
}
x <- c(6, 45, 27, 37, 25, 58, 22, 86, 15, 97)
Bubble_sort(x)
