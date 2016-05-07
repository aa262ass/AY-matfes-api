import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;
import java.awt.Graphics2D;
import java.awt.image.BufferedImage;
import java.awt.image.ImageFilter;
import java.awt.image.ImageProducer;
import java.awt.image.ImageProducer;
import java.awt.image.AreaAveragingScaleFilter;
import java.awt.Toolkit;
import java.awt.image.FilteredImageSource;

public class Resize{

  public static void main(String args[]){
    
    File fin = new File("input.jpg");
    File fout = new File("output.jpg");
    try{
      scaleImage(fin, fout, 0.5);
    }catch(IOException e){}
  }

  public static void scaleImage(File in, File out, double scale) throws IOException {
      BufferedImage org = ImageIO.read(in);
      ImageFilter filter = new AreaAveragingScaleFilter(
          (int)(org.getWidth() * scale), (int)(org.getHeight() * scale));
      ImageProducer p = new FilteredImageSource(org.getSource(), filter);
      java.awt.Image dstImage = Toolkit.getDefaultToolkit().createImage(p);
      BufferedImage dst = new BufferedImage(
          dstImage.getWidth(null), dstImage.getHeight(null), BufferedImage.TYPE_INT_RGB);
      Graphics2D g = dst.createGraphics();
      g.drawImage(dstImage, 0, 0, null);
      g.dispose();
      ImageIO.write(dst, "jpeg", out);
  }
}
