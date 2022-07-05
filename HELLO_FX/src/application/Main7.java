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

public class Main7 extends Application {
	TextField tfMine;
	TextField tfCom;
	TextField tfResult;

	@Override
	public void start(Stage primaryStage) {
		try {

			VBox root = (VBox) FXMLLoader.load(getClass().getResource("main7.fxml"));
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
		int idx = random.nextInt(3);
		String[] arr = {"가위","바위","보"};
		String com = arr[idx];
		
		tfCom.setText(com);

		if (me.equals(com)) {
			tfResult.setText("비김");
		} else if(me.equals("가위") && com.equals("보")
				||me.equals("바위") && com.equals("가위")
				||me.equals("보") && com.equals("바위")) {
			tfResult.setText("이김");
		}else{
			tfResult.setText("짐");
		}
	}

	public static void main(String[] args) {
		launch(args);
	}

}
