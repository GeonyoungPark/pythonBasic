package application;

import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

public class Main8 extends Application {
	TextField tf1, tf2;
	TextArea ta;

	@Override
	public void start(Stage primaryStage) {
		try {

			VBox root = (VBox) FXMLLoader.load(getClass().getResource("main8.fxml"));
			Scene scene = new Scene(root, 400, 400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();
			Button btn = (Button) scene.lookup("#btn");
			tf1 = (TextField) scene.lookup("#tf1");
			tf2 = (TextField) scene.lookup("#tf2");
			ta = (TextArea) scene.lookup("#ta");

			btn.setOnMouseClicked(new EventHandler<Event>() {

				@Override
				public void handle(Event event) {
					myClick();
				}
			});

		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	public void myClick() {
		String a = tf1.getText();
		String b = tf2.getText();

		int aa = Integer.parseInt(a);
		int bb = Integer.parseInt(b);

		String txt = "";

		for (int i = aa; i <= bb; i++) {
			txt += drawStar(i);
		}

		ta.setText(txt);

	}

	public String drawStar(int cnt) {
		String ret = "";
		for (int i = 0; i < cnt; i++) {
			ret += "*";
		}
		ret += "\n";

		return ret;
	}

	public static void main(String[] args) {
		launch(args);
	}

}
