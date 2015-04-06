︠839e0ac4-389d-4f54-b48c-d447bd247a76r︠
def primes(n):
    #At start, all values are mapped to 1 (potentially prime)
    dicti = {x: 1 for x in range(2, n+1)}
    for p in range(2,n + 1):
    #If p is potentially prime
        if dicti[p]==1:
            for i in range(p,(n/p) + 1):
    #This removes the multiples by setting their value to 0 (composite)
                dicti[i*p] = 0
        p+=1

    primes = []
    for key in dicti.keys():
        if dicti[key] == 1:
            primes.append(key)

    print primes
︡7d6b4a9c-1df6-41d5-966a-7c53e55fe37c︡{}︡{"stdout":"","done":true}︡
︠39949628-a83d-4e94-a7f7-d0658c18c384r︠

    %timeit primes(10000)
︡83c377ea-ed7b-4963-8b4e-02a8f23cacf0︡{}︡{"stdout":"25 loops, best of 3: 33.6 ms per loop"}︡{"stdout":"\n"}︡{"stdout":"","done":true}︡
︠ce3668e1-398d-4b33-8edf-09fc0434a0eer︠
%cython

cdef primes(n):
    #At start, all values are mapped to 1 (potentially prime)
    dicti = {x: 1 for x in range(2, n+1)}
    for p in range(2,n + 1):
    #If p is potentially prime
        if dicti[p]==1:
            for i in range(p,(n/p) + 1):
    #This removes the multiples by setting their value to 0 (composite)
                dicti[i*p] = 0
        p+=1

    primes = []
    for key in dicti.keys():
        if dicti[key] == 1:
            primes.append(key)

    print primes
︡5269dc84-a20d-40d4-b5fe-9d9102e56dcf︡{}︡{"file":{"show":false,"uuid":"77b0d143-fe65-427f-a4ab-2e2c6fc0014b","filename":"/home/0701b8e7/.sage/temp/u/28213/spyx/_home_0701b8e7__sage_temp_u_28213_dir_xD5BOx_a_pyx/_home_0701b8e7__sage_temp_u_28213_dir_xD5BOx_a_pyx_0.html"}}︡{"html":"<a href='/blobs//home/0701b8e7/.sage/temp/u/28213/spyx/_home_0701b8e7__sage_temp_u_28213_dir_xD5BOx_a_pyx/_home_0701b8e7__sage_temp_u_28213_dir_xD5BOx_a_pyx_0.html?uuid=77b0d143-fe65-427f-a4ab-2e2c6fc0014b' target='_new' class='btn btn-small '>Show auto-generated code >> </a>"}︡{"stdout":"","done":true}︡
︠3fc9bf02-89fb-44e1-beef-d77b158ed460r︠
 %timeit primes(10000)
︡2181f59b-a248-495c-b80e-41a1382e0b36︡{}︡{"stdout":"25 loops, best of 3: 19.6 ms per loop"}︡{"stdout":"\n"}︡{"stdout":"","done":true}︡
︠d0bff19c-b985-49a5-84f4-0dafdaa46893︠


