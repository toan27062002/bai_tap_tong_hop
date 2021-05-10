heapify <- function(arr,n,i)
{
  largest <- i   #Khoi tao lon nhat
  t <- 2*(i - 1) + 1   #Ben phai = 2*i + 1
  p <- 2*(i - 1) + 2   #Ben trai = 2*i + 2
  if((t<n) & (arr[largest]<arr[t]))
  {
    largest = t
  }
  if((p<n)&&(arr[largest]<arr[p]))
  {
    largest = p
  }
  if(largest != i)
  {
    arr <- replace(arr, c(i, largest), arr[c(largest, i)])
    arr <- heapify(arr, n, largest)
  }
  arr
}

heap_sort <- function(arr)
{
  n = length(arr)
  #Xay dung muc toi da
  for (i in (n/2):1) 
  {
    arr <- heapify(arr, n, i)
  }
  # Trich xuat tung phan tu mot
  for (i in n:1) {
    arr <- replace(arr, c(i, 1), arr[c(1, i)]) #Hoan doi
    arr <- heapify(arr, i, 1)
  }
  arr
}

arr <- sample(1:100)
heap_sort(arr)
