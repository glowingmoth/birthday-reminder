
document.addEventListener("DOMContentLoaded", function () {
    if (Notification.permission !== "granted")
      Notification.requestPermission();
  });

  function notifyMe() {
    if (!Notification) {
      alert("Desktop notifications not available in your browser");
      return;
    }

    if (Notification.permission !== "granted")
      Notification.requestPermission();
    else {
      const notification = new Notification("Reminder!", {
        icon:
          "https://img.icons8.com/office/16/000000/birthday.png",
        body: "It's someones birthday today!",
      });
      notification.onclick = function () {
        window.focus();
        this.close();
      };
    }
  }
console.log(Notification.permission);

