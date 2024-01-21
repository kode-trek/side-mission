import java.applet.Applet;
import java.awt.*;

public class hello_applet extends Applet {
	public void paint(Graphics g) {
		g.drawString("hello, java-applet!", 10, 50);
	}
}
