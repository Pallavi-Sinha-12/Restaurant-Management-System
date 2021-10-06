# Restaurant-Management-System
Object Oriented Designing of Restaurant Management System.

This is Object Oriented Design and Implementation of Restaurant Management System in Python language. I have tried to
write CLEAN CODE and tried to follow SOLID PRINCIPLES and apply some Design pattern like Factory Design Pattern, 
Singleton Design Pattern etc.

Some key points of this system - 

1. Admin can login with his password. He/she can add or remove employee and update their salary. He/she can remove
   table or add new table. He/she is also responsible for adding, updating or removing any item in menu. Admin can
   also do tasks of other employees.

2. A Receptionist can login with his/her password and do tasks like register customer, reserve a table, book a table.
   Before customer leaves they check payment status if paid or not. Then he/she records the customer details and
   payment amount in record history.

3. A waiter can login with his/her password and do tasks like accept order from customer sitting on a particular 
   table. He/she can show the menu to the customer and add items to the order according to the customer's wish. 
   He/she can check the current status of the order and can serve on order completion by the chef. After serving 
   he/she can show the bill to the customer and receive payment.

4. A chef can login with his/her password and see the pending orders. He/she chose an order and start preparing it
   after upadating that the order is being cooked. Upon completion he/she update that the order is completed and 
   go for preparing next order.

DETAILS OF ENUMS -

1. OrderStatus -> RECEIVED, PREPARING, COMPLETED, SERVED, CANCELED

2. TableStatus -> FREE, RESERVED, OCCUPIED

3. PaymentStatus -> UNPAID, PAID, REFUNDED 

4. TableType -> REGULAR, DELUX, SUPERDELUX

DETAILS OF CLASSES-

1. MenuItem -> Attributes - id, title, description, price

2. Menu -> This is Singleton class.
           Attributes - menuItems(contains all menuitems)
           Methods - GetMenuItem (get menu item by id), DisplayMenu (show menu items with all its attributes)

3. Order -> Attributes - OrderID, customer, waiter, status, OrderItems, creationtime

4. Payment -> Attributes - PaymentID, OrderID, Amount, PaymentStatus

5. Table -> Attributes - TableNumber, TableStatus, TableType

6. Account -> Attributes - id, password

7. Person -> Attributes - name, phone, email

8. Customer -> SuperClass - Person

9. Employee -> Superclass - Person
               Attributes - account

10. Chef -> Superclass - Employee
           Attributes - account

11. Waiter -> Superclass - Employee

12. Receptionist -> Superclass - Employee

13. Branch -> This is Singleton class.
             Attributes - name, address, Chefs, Tables, Receptionists, Waiters, Orders, Customers and Payments.

14. ValidateAccountChef ->Attributes - branch
                          Methods - CheckPassword (Used to check the password is correct or not of chef)

15. ValidateAccountWaiter ->  Attributes - branch
                              Methods - CheckPassword (Used to check the password is correct or not of waiter)

16. ValidateAccountReceptionist ->  Attributes - branch
                                    Methods - CheckPassword (Used to check the password is correct or not of receptionist)

17. ValidateAccount -> Attributes - branchname, address, EmployeeTypes
                       Methods - ValidatePassword (Used to validate password based on employee type provided. Use factory design pattern)

18. TableService -> Attributes - branch
                    Methods - AddTable (Used to add table in the branch of a particular type), RemoveTable(used to remove existing table)

19. MenuService -> Attributes - menu
                   Methods - AddMenuItems (add new items to the menu), RemoveMenuItems (to remove existing item from menu),
                             ShowMenu (dispaly menu), UpdatePrice (update price of a particular menu item)

20. EmployeeManagementService -> Abstract class
                                 Attributes - branch
                                 Methods - AddEmployee (add chef in the branch), RemoveEmployee (to remove existing employee),
                                           UpdateSalary (update salary of an employee)

21. ChefManagementService -> Superclass - EmployeeManagementService

22. ReceptionistManagementService -> SuperClass - EmployeeManagementService

23. WaiterManagementService -> SuperClass - EmployeeManagementService

24. WelcomeService -> Attributes - branch
                      Methods - ShowFreeTable (Used to show free table of a particular type), ReserveTable (to reserve a table)
                                OccupyTable(used to occupy table)

25. OrderService -> Attributes - branch, OrderID
                    Methods - ReceiveOrder (to receive order), GetOrderStatus (to get current status of order), ServeOrder(to servethe order)
                              CancelOrder (to cancel order), ClearOrder (remove order from current cache/storage)

26. CustomerService -> SuperClass - OrderService
                       Attributes - menu
                       Methods - ShowMenu (to display menu to the customer), AddOrderItems (to add items in order)

27. CookingService -> Attributes - branch
                      Methods - GetPendingOrdersList(Display all orders yet to be cooked), CookOrder (to start cooking order) 
                      CompleteOrder (to update completed after cooking)

28. BillService -> Attributes - branch, order, GST
                   Methods - CalculateBill (return total bill of an order), ShowBill(Display price of each item along with total bill)

29. PaymentService -> SuperClass - Payment
                      Attributes - branch
                      Methods - ReceivePayment (to receive payment), GetBillAmount (display payment amount to be given),
                                Refund (to refund payment), UpdatePayment (update payment status and amount with table number of customer)

30. CheckoutService -> Attributes - branch
                       Methods - CheckPayment (to check whether payment is made or not for a particular table number occupied by customer)
                                 Freetable (update that table is free), RecordInfo( to record details of customer with amount paid)
                                 ClaerCustomersAndPayments (clear payment and customer objects from current storage)

31. AdminService -> Encapsulating all the services to be performed by admin in one unit
                    Attributes - password
                    Methods - ValidatePassword (Check if password provided is matched), ShowServices (To show all services that can be
                    accessed by admin), ReceptionistManagementService (to access ReceptionistManagementService methods and attributes),
                    ChefManagementService (to access ChefManagementService methods and attricutes)
                    WaiterManagementService (to access WaiterManagementService methods and attributes)

32. ReceptionistService -> Encapsulating all the services to be performed by receptionist in one unit
                     Attributes - id, password, branchname, address
                     Methods - ShowServices (dispaly all services to be performed by waiter), ValidatePassword (Check if password provided
                     id correct or not), WelcomeService (to access WelcomeService methods and attributes), CheckoutService (to access 
                     CheckoutService methods and attributes)


33. WaiterService -> Encapsulating all the services to be performed by waiter in one unit
                     Attributes - id, password, branchname, address
                     Methods - ShowServices (dispaly all services to be performed by waiter), ValidatePassword (Check if password provided
                     id correct or not), CustomerService (to access CustomerService methods and attributes), BillService (to access 
                     BillService methods and attributes), PaymentService (to access Payment Service methods and attributes)

34. ChefService -> Encapsulating all the services to be performed by chef in one unit
                     Attributes - id, password, branchname, address
                     Methods - ShowServices (dispaly all services to be performed by waiter), ValidatePassword (Check if password provided
                     id correct or not), CookingService (to access CookingService methods and attributes)


                                

Note - For now it is in the form of code only and I have not deployed it into a website. You can check the
       ExampleRun.pynb file to view how it works. In this project my main focus was to make this system by following 
       SOLID principles and applying PYTHON DESIGN PATTERNS.
   
