function main(workbook: ExcelScript.Workbook)
{
  let selectedSheet = workbook.getActiveWorksheet();
  selectedSheet.getRange("<INSERT EXCEL RANGE HERE>").setNumberFormat("<SET NUMBER FORMAT>")
  selectedSheet.getUsedRange().getFormat().autofitColumns();
  let range = selectedSheet.getUsedRange();
  let rangeValues = range.getValues();
  let rowCount = range.getRowCount();
  for (let i = 1; i < rowCount; i++){
    if (rangeValues[i][3]){ //Insert column index here
      let positiveValue = Math.abs(rangeValues[i][3] as number);
      selectedSheet.getCell(i,3).setValue(positiveValue);
    }

    if (rangeValues[i][4]){ //Insert column index here
      let positiveValue = Math.abs(rangeValues[i][4] as number);
      selectedSheet.getCell(i,4).setValue(positiveValue);
    }

    //Insert additional column indexes below if this process needs to be looped over more columns
  }
