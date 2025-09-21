package com.example.myapplication123;

import android.annotation.SuppressLint;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_main);
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
            Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
            return insets;
        });


        TextView Pas1 = findViewById(R.id.has1);
        TextView Pas2 = findViewById(R.id.has2);


        @SuppressLint({"MissingInflatedId", "LocalSuppress"}) TextView Dowys = findViewById(R.id.wysw);
        Button przycisk = findViewById(R.id.button);

        TextView Mail = findViewById(R.id.maila);


        //mail musi byc z @ inaczej niepoprawny mail


przycisk.setOnClickListener(new View.OnClickListener() {
    @SuppressLint("SetTextI18n")
    @Override
    public void onClick(View v) {
        String tekst1 = Pas1.getText().toString();
        String tekst2 = Pas2.getText().toString();
        String maila = Mail.getText().toString();

        if(!tekst1.equals(tekst2)){
            Dowys.setText("Hasla sa rozne");

        }else if(!maila.contains("@")){
            Dowys.setText("Mail niepoprawny");

        }else{
            Dowys.setText("Witaj" + maila);
        }

    }
});




    }
}