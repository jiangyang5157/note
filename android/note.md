# Android

## MVC & MVP & MVVM
https://www.jianshu.com/p/ffcb84dc4ebc

## ANR
产生原因：
- (1)5s内无法响应用户输入事件(例如键盘输入, 触摸屏幕等).
- (2)BroadcastReceiver在10s内无法结束
- (3)Service 20s内无法结束（低概率）
解决方式：
- (1)不要在主线程中做耗时的操作，而应放在子线程中来实现。如onCreate()和onResume()里尽可能少的去做创建操作。
- (2)应用程序应该避免在BroadcastReceiver里做耗时的操作或计算。
- (3)避免在Intent Receiver里启动一个Activity，因为它会创建一个新的画面，并从当前用户正在运行的程序上抢夺焦点。
- (4)service是运行在主线程的，所以在service中做耗时操作，必须要放在子线程中。

## Context
- Context是一个抽象基类。在翻译为上下文，也可以理解为环境，是提供一些程序的运行环境基础信息。Context下有两个子类，ContextWrapper是上下文功能的封装类，而ContextImpl则是上下文功能的实现类。而ContextWrapper又有三个直接的子类， ContextThemeWrapper、Service和Application。其中，ContextThemeWrapper是一个带主题的封装类，而它有一个直接子类就是Activity，所以Activity和Service以及Application的Context是不一样的，只有Activity需要主题，Service不需要主题。Context一共有三种类型，分别是Application、Activity和Service。这三个类虽然分别各种承担着不同的作用，但它们都属于Context的一种，而它们具体Context的功能则是由ContextImpl类去实现的，因此在绝大多数场景下，Activity、Service和Application这三种类型的Context都是可以通用的。不过有几种场景比较特殊，比如启动Activity，还有弹出Dialog。出于安全原因的考虑，Android是不允许Activity或Dialog凭空出现的，一个Activity的启动必须要建立在另一个Activity的基础之上，也就是以此形成的返回栈。而Dialog则必须在一个Activity上面弹出（除非是System Alert类型的Dialog），因此在这种场景下，我们只能使用Activity类型的Context，否则将会出错。
- getApplicationContext()和getApplication()方法得到的对象都是同一个application对象，只是对象的类型不一样。
- Context数量 = Activity数量 + Service数量 + 1 （1为Application）

## LaunchMode
- standard 模式
  - 这是默认模式，每次激活Activity时都会创建Activity实例，并放入任务栈中。使用场景：大多数Activity。
- singleTop 模式
  - 如果在任务的栈顶正好存在该Activity的实例，就重用该实例( 会调用实例的 onNewIntent() )，否则就会创建新的实例并放入栈顶，即使栈中已经存在该Activity的实例，只要不在栈顶，都会创建新的实例。使用场景如新闻类或者阅读类App的内容页面。
- singleTask 模式
  - 如果在栈中已经有该Activity的实例，就重用该实例(会调用实例的 onNewIntent() )。重用时，会让该实例回到栈顶，因此在它上面的实例将会被移出栈。如果栈中不存在该实例，将会创建新的实例放入栈中。使用场景如浏览器的主界面。不管从多少个应用启动浏览器，只会启动主界面一次，其余情况都会走onNewIntent，并且会清空主界面上面的其他页面。
- singleInstance 模式
  - 在一个新栈中创建该Activity的实例，并让多个应用共享该栈中的该Activity实例。一旦该模式的Activity实例已经存在于某个栈中，任何应用再激活该Activity时都会重用该栈中的实例( 会调用实例的 onNewIntent() )。其效果相当于多个应用共享一个应用，不管谁激活该 Activity 都会进入同一个应用中。使用场景如闹铃提醒，将闹铃提醒与闹铃设置分离。singleInstance不要用于中间页面，如果用于中间页面，跳转会有问题，比如：A -> B (singleInstance) -> C，完全退出后，在此启动，首先打开的是B。

##  Activity 的启动模式
- standard: 系统的默认模式，一次跳转即会生成一个新的实例。假设有一个activity命名为MainActivity，执行语句：
startActivity(new Intent(MainActivity.this, MainActivity.class))后，MainActivity将跳转到另外一个MainActivity，也就是现在的Task栈里面有MainActivity的两个实例。按返回键后你会发现仍然是在MainActivity（第一个）里面。
- singleTop: singleTop 跟standard 模式比较类似。如果已经有一个实例位于Activity栈的顶部时，就不产生新的实例，而只是调用Activity中的newInstance()方法。如果不位于栈顶，会产生一个新的实例。例：当MainActivity为 singleTop 模式时，执行跳转后栈里面依旧只有一个实例，如果现在按返回键程序将直接退出。
- singleTask: singleTask模式和后面的singleInstance模式都是只创建一个实例的。在这种模式下，无论跳转的对象是不是位于栈顶的activity，程序都不会生成一个新的实例（当然前提是栈里面已经有这个实例）。这种模式相当有用，在以后的多activity开发中，经常会因为跳转的关系导致同个页面生成多个实例，这个在用户体验上始终有点不好，而如果你将对应的activity声明为 singleTask 模式，这种问题将不复存在。
- singleInstance: 设置为 singleInstance 模式的 activity 将独占一个task（感觉task可以理解为进程），独占一个task的activity与其说是activity，倒不如说是一个应用，这个应用与其他activity是独立的，它有自己的上下文activity。

## java中==和equals和hashCode的区别
- 基本数据类型的==比较的值相等. 
- 类的==比较的内存的地址，即是否是同一个对象，在不覆盖equals的情况下，同比较内存地址，原实现也为 == ，如String等重写了equals方法.
hashCode也是Object类的一个方法。返回一个离散的int型整数。在集合类操作中使用，为了提高查询速度。（HashMap，HashSet等比较是否为同一个）
- 如果两个对象equals，Java运行时环境会认为他们的hashcode一定相等。
- 如果两个对象不equals，他们的hashcode有可能相等。
- 如果两个对象hashcode相等，他们不一定equals。
- 如果两个对象hashcode不相等，他们一定不equals。
- Object类的equal和hashCode方法重写，为什么？
  - 1、如果两个对象相同（即用equals比较返回true），那么它们的hashCode值一定要相同；
  - 2、如果两个对象的hashCode相同，它们并不一定相同(即用equals比较返回false)
  - 由于为了提高程序的效率才实现了hashcode方法，先进行hashcode的比较，如果不同，那没就不必在进行equals的比较了，这样就大大减少了equals比较的次数，这对比需要比较的数量很大的效率提高是很明显的

## String、StringBuffer、StringBuilder区别 
- String:字符串常量 不适用于经常要改变值得情况，每次改变相当于生成一个新的对象
- StringBuffer:字符串变量 （线程安全）
- StringBuilder:字符串变量（线程不安全） 确保单线程下可用，效率略高于StringBuffer

## 进程和线程的区别
- 进程是cpu资源分配的最小单位，线程是cpu调度的最小单位。
- 进程之间不能共享资源，而线程共享所在进程的地址空间和其它资源。
- 一个进程内可拥有多个线程，进程可开启进程，也可开启线程。
- 一个线程只能属于一个进程，线程可直接使用同进程的资源,线程依赖于进程而存在。
- 线程是进程的子集，一个进程可以有很多线程，每条线程并行执行不同的任务。不同的进程使用不同的内存空间，而所有的线程共享一片相同的内存空间。别把它和栈内存搞混，每个线程都拥有单独的栈内存用来存储本地数据。


## Serializable 和Parcelable 的区别 
- Serializable Java 序列化接口 在硬盘上读写 读写过程中有大量临时变量的生成，内部执行大量的i/o操作，效率很低。
- Parcelable Android 序列化接口 效率高 使用麻烦 在内存中读写（AS有相关插件 一键生成所需方法） ，对象不能保存到磁盘中

## 5种方式存储数据
- SharedPreferences
- 文件存储数据
- SQLite
- 使用ContentProvider存储数据；
- 网络存储数据

## Service
- 通过startService启动Service：onCreate、onStartCommand、onDestory。
- 通过bindService绑定Service：onCreate、onBind、onUnbind、onDestory。

## 如何一次性退出所有打开的Activity
编写一个Activity作为入口，当需要关闭程序时，可以利用Activity的SingleTop模式跳转该Activity，它上面的所有Activity都会被销毁掉。然后再将该Activity关闭。或者再跳转时，设置intent.setFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP);这样也能将上面的Activity销毁掉。

## ContentProvide
使用ContentProvider 可以将数据共享给其他应用，让除本应用之外的应用也可以访问本应用的数据。它的底层是用SQLite 数据库实现的，所以其对数据做的各种操作都是以Sql实现，只是在上层提供的是Uri。

## 显式intent和隐式intent的区别是什么
Android基本的设计理念是鼓励减少组件间的耦合，因此Android提供了Intent (意图) ，Intent提供了一种通用的消息系统，它允许在你的应用程序与其它的应用程序间传递Intent来执行动作和产生事件。使用Intent可以激活Android应用的三个核心组件：活动、服务和广播接收器。作为一个完整的消息传递机制，Intent不仅需要发送端，还需要接收端。
- 显式Intent定义：对于明确指出了目标组件名称的Intent，我们称之为显式Intent。
- 隐式Intent定义：对于没有明确指出目标组件名称的Intent，则称之为隐式Intent。
- 说明：Android系统使用IntentFilter 来寻找与隐式Intent相关的对象。

## Handler 机制的原理
- android提供了 Handler 和 Looper 来满足线程间的通信。
- Handler 先进先出原则。
- Looper类用来管理特定线程内对象之间的消息交换(Message Exchange)。
- Looper: 一个线程可以产生一个Looper对象，由它来管理此线程里的Message Queue(消息队列)。
- Handler: 你可以构造Handler对象来与Looper沟通，以便push新消息到Message Queue里;或者接收Looper从Message Queue取出)所送来的消息。
- Message Queue(消息队列):用来存放线程放入的消息。
- 线程：UI thread 通常就是main thread，而Android启动程序时会替它建立一个Message Queue。
