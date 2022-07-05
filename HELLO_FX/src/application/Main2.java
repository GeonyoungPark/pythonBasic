package application;



import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

public class Main2 extends Application {
	TextField tf;
	@Override
	public void start(Stage primaryStage) {
		try {

			VBox root = (VBox) FXMLLoader.load(getClass().getResource("main2.fxml"));
			Scene scene = new Scene(root, 400, 400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();
			Button btn = (Button) scene.lookup("#btn");
			tf = (TextField) scene.lookup("#tf");
		
			
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
		int getNum = Integer.parseInt(tf.getText());
		getNum++;
		tf.setText(getNum+"");
	}

	public static void main(String[] args) {
		launch(args);
	}

}
