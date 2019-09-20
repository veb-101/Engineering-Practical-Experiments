import java.awt.*;
import java.awt.event.*;
import java.applet.*;

/*<applet code="que8" width="300" height="100" > </applet>*/

public class que8 extends Applet implements MouseMotionListener{
    String msg = "";
    int mx =0, my = 0;

    public void init(){
        addMouseMotionListener(this);
    }
    public void mouseDragged(MouseEvent m){
        mx = m.getX();
        my = m.getY();
        msg = "*";
        showStatus("Dragging Mouse at " + mx + ", "+ my);
        repaint();
    }
    public void mouseMoved(MouseEvent m){
        showStatus("Mouse Moving at " + m.getX() + ", "+ m.getY());
    }
    public void paint(Graphics g){
        g.drawString(msg, mx, my);
    }
}
