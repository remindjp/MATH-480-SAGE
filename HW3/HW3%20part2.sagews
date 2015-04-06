︠0c9d6b25-f5d1-4717-8ad5-4c953abed71br︠
def problem2(n):
    sum =0
    for i in range(n + 1):
        sum += i**2

    return sum

%timeit problem2(10000)
print problem2(10000)
︡db82b366-1b1b-42d1-b40c-ef04e9f730fc︡{}︡{"stdout":"125 loops, best of 3: 5.2 ms per loop"}︡{"stdout":"\n"}︡{"stdout":"333383335000"}︡{"stdout":"\n"}︡{"stdout":"","done":true}︡
︠989e671e-452d-4a50-a8f3-5164cdf5de4er︠
%cython

cpdef problem2_c(int n):
    cdef long sum =0
    for i in range(n + 1):
        sum += i**2

    return sum
︡3477fc51-82c8-4fc9-87e5-b054e15ae054︡{}︡{"file":{"show":false,"uuid":"8e02542d-92ef-4b50-8b14-c0ae3ac617c5","filename":"/home/0701b8e7/.sage/temp/u/5844/spyx/_home_0701b8e7__sage_temp_u_5844_dir_1At5N3_a_pyx/_home_0701b8e7__sage_temp_u_5844_dir_1At5N3_a_pyx_0.html"}}︡{"html":"<a href='/blobs//home/0701b8e7/.sage/temp/u/5844/spyx/_home_0701b8e7__sage_temp_u_5844_dir_1At5N3_a_pyx/_home_0701b8e7__sage_temp_u_5844_dir_1At5N3_a_pyx_0.html?uuid=8e02542d-92ef-4b50-8b14-c0ae3ac617c5' target='_new' class='btn btn-small '>Show auto-generated code >> </a>"}︡{"stdout":"","done":true}︡
︠ca207f50-89a8-424e-ab77-ec1ebad7bb8fr︠
%timeit problem2_c(10000)
︡7bbf39b0-6699-46f1-8cd4-86170b6069c4︡{}︡{"stdout":"625 loops, best of 3: 871 µs per loop"}︡{"stdout":"\n"}︡{"stdout":"","done":true}︡
︠d33fc66e-ecdb-4bff-a953-9b42e6a788d1r︠



