
import JSEncrypt from 'jsencrypt'

const key = `-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCMoSewxBrnXFZtdTpUYfJD1RME
boivgZrcrCr+8/cOpSpsqCC/WYA3d0p8vbNAFvSJzDK8pL9ldhVVTmQQLY8uQsQU
3rCxVGBQrvZmy9Fr/qEx+L9X/NQCU4KSArAVboHTzp5C4nyttDaCVcdCaRE5Ii0O
QLDomWKv2f9je6LSpQIDAQAB
-----END PUBLIC KEY-----`
export default str => {
  let encrypt = new JSEncrypt()
  encrypt.setPublicKey(key)
  // console.log(str)
  return encrypt.encrypt(str)
}
