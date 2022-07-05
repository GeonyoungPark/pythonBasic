package application;

import java.util.Random;

import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

public class Main5 extends Application {
	TextField tfMine;
	TextField tfCom;
	TextField tfResult;

	@Override
	public void start(Stage primaryStage) {
		try {

			VBox root = (VBox) FXMLLoader.load(getClass().getResource("main5.fxml"));
			Scene scene = new Scene(root, 400, 400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();
			Button btn = (Button) scene.lookup("#btn");
			tfMine = (TextField) scene.lookup("#tf_mine");
			tfCom = (TextField) scene.lookup("#tf_com");
			tfResult = (TextField) scene.lookup("#tf_result");

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
		String me = tfMine.getText();
		Random random = new Random();
		int idx = random.nextInt(2);
		String com ="";
		if (idx == 0) {
			com = "짝";
		} else {
			com = "홀";
		}
		tfCom.setText(com);

		if (me.equals(com)) {
			tfResult.setText("이김");
		} else {
			tfResult.setText("짐");

		}
	}

	public static void main(String[] args) {
		launch(args);
	}

}
