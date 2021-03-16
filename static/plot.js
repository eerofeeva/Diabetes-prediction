function DrawGraph(user)
{
  function PositiveData(subject) {
    return parseInt(subject.Outcome) > 0;
  }

  var filteredDiabetesPos = DiabetesClean.filter(PositiveData);
  // console.log(filteredDiabetesPos);

  var AgePos = filteredDiabetesPos.map(subject => subject.Age);
  // console.log(AgePos);

  var BMIPos = filteredDiabetesPos.map(subject => subject.BMI);
  // console.log(BMIPos);

  function NegativeData(subject) {
    return parseInt(subject.Outcome) === 0;
  }

  var filteredDiabetesNeg = DiabetesClean.filter(NegativeData);
  // console.log(filteredDiabetesNeg);

  var AgeNeg = filteredDiabetesNeg.map(subject => subject.Age);
  // console.log(AgeNeg);

  var BMINeg = filteredDiabetesNeg.map(subject => subject.BMI);
  // console.log(BMINeg);

  var trace1 = {
    x: AgePos,
    y: BMIPos,
    mode: 'markers',
    type: "scatter",
    name: 'Diabetes'
  };

  var trace2 = {
    x: AgeNeg,
    y: BMINeg,
    mode: 'markers',
    type: "scatter",
    name: 'No Diabetes'
  };

  var trace3 = {
    x: [user.age], //age
    y: [user.bmi], //bmi
    mode: 'markers',
    type: "scatter",
    name: 'User Data',
    marker: { size: 12 }
  }

  var data = [trace1, trace2, trace3];

  var layout = {
    title: "Age vs. BMI of People with and without Diabetes",
    xaxis: { title: "Age" },
    yaxis: { title: "BMI"}
  };

  Plotly.newPlot("scatter-plot", data, layout);
}

// // Glucose Plot

//var GlucosePos = filteredDiabetesPos.map(subject => subject.Glucose);
// console.log(GlucosePos);

var GlucoseNeg = filteredDiabetesNeg.map(subject => subject.Glucose);
// console.log(GlucoseNeg);


var trace4 = {
  x: AgePos,
  y: GlucosePos,
  mode: 'markers',
  type: "scatter",
  name: 'Diabetes'
};

var trace5 = {
  x: AgeNeg,
  y: GlucoseNeg,
  mode: 'markers',
  type: "scatter",
  name: 'No Diabetes'
};

var trace6 = {
  x: [user.age], //age
  y: [user.glucose], //glucose
  mode: 'markers',
  type: "scatter",
  name: 'User Data',
  marker: { size: 12 }
}

var data2 = [trace4, trace5, trace6];

var layout2 = {
  title: "Age vs. Glucose of People with and without Diabetes",
  xaxis: { title: "Age" },
  yaxis: { title: "Glucose"}
};

Plotly.newPlot("scatter-plot2", data2, layout2);