import createEmployeesObject from './11-createEmployeesObject.js';
import createReportObject from './12-createReportObject.js';

const engineering = ['John Doe', 'Guillaume Salva'];
const marketing = ['Agatha Christie', 'Jason Leverson'];
const design = ['Kanye East', 'Jay Li'];

test('createReportObject returns the correct object', () => {
  const employees = {
    ...createEmployeesObject('engineering', engineering),
    ...createEmployeesObject('marketing', marketing),
    ...createEmployeesObject('design', design),
  };

  const holbertonEmployees = {
    engineering,
    marketing,
    design,
  };

  const report = createReportObject(employees);

  expect(report.allEmployees).toStrictEqual(holbertonEmployees);
  expect(report.getNumberOfDepartments(report.allEmployees)).toStrictEqual(3);
});
