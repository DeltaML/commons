from Pyfhel import Pyfhel, PyCtxt
import tempfile


def test_save_and_load_pk():
    pyfhel = Pyfhel()
    pyfhel.contextGen(p=1964769281, m=8192, base=2, sec=192, flagBatching=True)
    pyfhel.keyGen()
    pyfhel.rotateKeyGen(60)
    pyfhel.relinKeyGen(60, 4)
    # encrypt something
    ctxt = pyfhel.encryptInt(42)
    tmp = tempfile.NamedTemporaryFile()
    ctxt.save(tmp.name)
    # load from temporary file
    loaded = PyCtxt()
    loaded.load(tmp.name)
    assert pyfhel.decryptInt(loaded) == 42


def test_mult_iter():
    pyfhel = Pyfhel()
    pyfhel.contextGen(p=1964769281, m=32768, base=2, sec=192, intDigits=150, fracDigits=42)
    pyfhel.keyGen()
    pyfhel.rotateKeyGen(60)
    pyfhel.relinKeyGen(30, 2)
    ctxt3 = pyfhel.encryptFrac(1.0)
    ctxt4 = pyfhel.encryptFrac(1.1)

    ctxt_mult3 = pyfhel.multiply(ctxt3, ctxt3, in_new_ctxt=True)
    pyfhel.relinearize(ctxt_mult3)
    for i in range(10):
        pyfhel.multiply(ctxt_mult3, ctxt4)
        pyfhel.relinearize(ctxt_mult3)
    print(ctxt_mult3.size())
    number = round(pyfhel.decryptFrac(ctxt_mult3), 2)
    print(number)
    assert number == 17.44


#test_save_and_load_pk()
test_mult_iter()
