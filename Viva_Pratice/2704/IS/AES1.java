import javax.crypto.Cipher;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;
public class AES1 {
    static String IV = "AAAAAAAAAAAAAAAA";
    static String plainText = "test text 123\u0000\u0000\u0000";
    static String key = "0123456789abcdef";

    public static void main(String[] args)throws Exception{
        byte[] cipher = encrypt(plainText, key);
        for (int i = 0; i < cipher.length; i++) {
            System.out.print(new Integer(cipher[i]) + " ");
        }
        System.out.print("\n");
        String decrypt = decrypt(cipher, key);
        System.out.println("decrypt: " + decrypt);
    }

    public static byte[] encrypt(String plainText, String encryptionKey) throws Exception{
        
        Cipher cipher = Cipher.getInstance("AES/CBC/NoPadding","SunJCE");
        SecretKeySpec key1 = new SecretKeySpec(encryptionKey.getBytes("UTF-8"), "AES");
        cipher.init(Cipher.ENCRYPT_MODE, key1, new IvParameterSpec(IV.getBytes("UTF-8")));
        return cipher.doFinal(plainText.getBytes("UTF8"));

    }

    public static String decrypt(byte[] cipherText, String encryptionKey) throws Exception{
        Cipher cipher = Cipher.getInstance("AES/CBC/NoPadding", "SunJCE");
        SecretKeySpec key1 = new SecretKeySpec(encryptionKey.getBytes("UTF8"), "AES");
        cipher.init(Cipher.DECRYPT_MODE, key1, new IvParameterSpec(IV.getBytes("UTF8")));
        return new String(cipher.doFinal(cipherText), "UTF8");
    }
    
}
