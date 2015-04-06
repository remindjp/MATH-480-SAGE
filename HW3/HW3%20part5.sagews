︠50ba52dc-44e4-45c8-beba-fa897ecedb29r︠
def multiply(a,b):
    #4x4 square matrix so m = n
    n = len(a)
    c = [[0 for y in range(n)] for x in range(n)]
    total = 0
    for y in range(n):
        for x in range(n):
            for i in range(n):
                total+=a[x][i]*b[i][y]
                c[x][y]=total
            total = 0
    return c

%timeit multiply([[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]], [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]])
︡32d26244-9543-4686-bea0-aee288d34a22︡{}︡{"stdout":"625 loops, best of 3: 46.3 µs per loop"}︡{"stdout":"\n"}︡{"stdout":"","done":true}︡
︠2fb03c6e-035d-4f65-b031-411835e98ae7r︠
%cython

cpdef multiply(a,b):
    #4x4 square matrix so m = n
    cpdef int n = len(a)
    c = [[0 for y in range(n)] for x in range(n)]
    total = 0
    for y in range(n):
        for x in range(n):
            for i in range(n):
                total+=a[x][i]*b[i][y]
                c[x][y]=total
            total = 0
    return c


︡c7b5d5ac-d72a-43de-9705-3c75854dee76︡{}︡{"file":{"show":false,"uuid":"be59df5a-980c-4c09-aa1a-d5d8c2b2f488","filename":"/home/0701b8e7/.sage/temp/u/8016/spyx/_home_0701b8e7__sage_temp_u_8016_dir__2ZZSa_a_pyx/_home_0701b8e7__sage_temp_u_8016_dir__2ZZSa_a_pyx_0.html"}}︡{"html":"<a href='/blobs//home/0701b8e7/.sage/temp/u/8016/spyx/_home_0701b8e7__sage_temp_u_8016_dir__2ZZSa_a_pyx/_home_0701b8e7__sage_temp_u_8016_dir__2ZZSa_a_pyx_0.html?uuid=be59df5a-980c-4c09-aa1a-d5d8c2b2f488' target='_new' class='btn btn-small '>Show auto-generated code >> </a>"}︡{"stdout":"","done":true}︡
︠e1962279-2280-4ef2-a14f-e61a84531f46r︠
%timeit multiply([[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]], [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]])
︡284bda21-5d7d-4fcd-943c-4cb79a651eb2︡{}︡{"stdout":"625 loops, best of 3: 29.4 µs per loop"}︡{"stdout":"\n"}︡{"stdout":"","done":true}︡
︠79c5c796-b9f9-4d6c-b7db-d9d3b354de85︠
