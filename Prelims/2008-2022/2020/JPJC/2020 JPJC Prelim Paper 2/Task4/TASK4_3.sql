SELECT SALE.SaleDate, SALESPERSON.SalesPersonName, CUSTOMER.CustomerName, SALE.Amount
FROM SALE, SALESPERSON,CUSTOMER
WHERE SALE.CustomerID = CUSTOMER.CustomerID
AND SALE.SalesPersonID = SALESPERSON.SalesPersonID
AND SALESPERSON.OfficeID = 1;