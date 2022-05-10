import javax.crypto.Cipher;
import javax.crypto.IvParameterSpec;
import javax.crypto.SecretKeySpec;

public class AES1{
    static String IV = "AAAAAAAAAAAAAAAA";
    static String plainText = "test text 123\u0000\u0000\u0000";
    static String key = "0123456789abcdef";
    public static  void main(String[] args){
        byte[] cipher = encrypt(plainText, key);
        System.out.println(cipher);
    }

    public static byte[] encrypt(String plainText, String key) throws Exception{
        Cipher cipher = new Cipher.getInstance("AES/CBC/NoPadding", "SunJCE");
        SecretKeySpec secretKey = new SecretKeySpec(key.getBytes(charSetName = "UTF8"), "AES");
        cipher.init(Cipher.ENCRYPT_MODE, secretKey, new IvParameterSpec(IV.getBytes(charSetName = "UTF8"))); 
        return cipher.doFinal(plainText.getBytes(charSetName = "UTF8"));   
    }

}