//code to create music player in java?
import java.io.File;

import javafx.scene.media.Media;
import javafx.scene.media.MediaPlayer;

public class MainClass {

    public static void main(String[] args) {
        
        com.sun.javafx.application.PlatformImpl.startup(()->{});
        
        Media sound = new Media(new File("C:\\Users\\SomeUser\\Desktop\\someFile.mp3").toURI().toString());
        MediaPlayer player = new MediaPlayer(sound);
        player.play();
        
        try {
            Thread.sleep(20000); //don't exit too early
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        
        com.sun.javafx.application.PlatformImpl.exit();
    }
}


InputStream in = null;
try {
    in = new FileInputStream("someFile.wav");
} catch (FileNotFoundException e) {
    e.printStackTrace();
}
AudioStream as = null;
try {
    as = new AudioStream(in);
} catch (IOException e) {
    e.printStackTrace();
}
AudioPlayer.player.start(as);


