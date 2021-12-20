/*
    Below is a straightforward example of Tiling optimization
    The first snippet is without chunking
    The second snippet is with chunking
    Tile size is a power of 2
    These are purely snippets without the full code, will not compile
    Full documentation in the 3300 Project1 Task C folder
*/

//--WITHOUT TILING OPTIMIZATION--//
 double sum = 0;

    // Repeat multiple times
    for(r = 0; r < repeats; r++) {
#pragma omp parallel for private(sum, k, j)
        for(i = 0; i < N; i++) {
            for(j = 0; j < N; j++) {
                sum = 0;

                for(k = 0; k < N; k++) {
                    sum += matrixA[i*N + k] * matrixB[k*N + j];
                }

                matrixC[i*N + j] = (alpha * sum) + (beta * matrixC[i*N + j]);
            }
        }
    }

//--WITH TILING OPTIMIZATION--//
double sum = 0;
    int chunkSize;
    int jT, kT;
    int size1 = 2048;
    int size2 = 4096;
    int size3 = 8192;

    if(N <= size1){
        chunkSize = 64;
    }else if(N <= size2 && N > size1){
        chunkSize = 64;
    }else if(N <= size3 && N > size2){
        chunkSize = 64;
    }else{
        chunkSize = 512;
    }

    // Repeat multiple times
    for(r = 0; r < repeats; r++){
  #pragma omp parallel for private(sum, k, j)
        for(jT= 0; jT < N;jT = jT + chunkSize){
            for(kT = 0; kT < N;kT = kT + chunkSize){
                for(i = 0; i < N; i++){
                    for(j= jT; j < jT + chunkSize -1; j++){
                        sum = 0;
                        for(k = kT; k < kT + chunkSize -1; k++){
                            sum += matrixA[i*N + k] * matrixB[k*N + j];
                        }

                         matrixC[i*N + j] = (alpha * sum) + (beta * matrixC[i*N + j]);
                    }
                }
                
            }
            
        }      
    }
