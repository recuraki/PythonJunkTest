
libssl-dev
```c++
Objects/dictobject.c

static Py_ssize_t
find_empty_slot(PyDictKeysObject *keys, Py_hash_t hash)
{
    assert(keys != NULL);
    const size_t mask = DK_MASK(keys);
    size_t i = hash & mask;
    Py_ssize_t ix = dictkeys_get_index(keys, i);
    printf("find_empty_slot %lx %lx %lx\n", mask, i, ix);
    printf("find_empty_slot inputhash %lx\n", hash);
    for (size_t perturb = hash; ix >= 0;) {
        perturb >>= PERTURB_SHIFT;
        i = (i*5 + perturb + 1) & mask;
        printf("loopb  key:%lx per:%lx i:%lx ix:%lx\n", keys, perturb,i , ix);
        ix = dictkeys_get_index(keys, i);
        printf("loopa  key:%lx per:%lx i:%lx ix:%lx\n", keys, perturb,i , ix);
    }
    printf("find_empty_slot RES %lx %lx %lx\n", mask,i , ix);
    return i;
}res
```