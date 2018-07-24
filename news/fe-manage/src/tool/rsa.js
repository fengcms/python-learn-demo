
import JSEncrypt from 'jsencrypt'

const key = `-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDIF5xV6/5+K2NMEXHypNzrUTYA
MTSSqQCAgbVmp7IUYD2HIqb80q8Z6GgKLSf2Qafqq5Qrgtb3nRYA796M2hAcIre/
Hth8+6tXu+34z+4QAsxjZdJhbyL/fcRpkRd2cmY8jXPoNafUMzO2pRJeSVP4glOf
6ew31S9BJz8YHBQmDQIDAQAB
-----END PUBLIC KEY-----`
export default str => {
  let encrypt = new JSEncrypt()
  encrypt.setPublicKey(key)
  // console.log(str)
  return encrypt.encrypt(str)
}
