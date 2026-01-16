# Power Apps Wrapper (Launcher)

This wrapper opens your Streamlit app from a Canvas app using the `Launch()` function.

## Steps (Canvas App)
1. Go to **make.powerapps.com** → **Apps** → **New app** → **Canvas app**.
2. Add a **Button** control to *Screen1*.
3. Set the **OnSelect** property to:
```powerfx
Launch("https://YOUR-STREAMLIT-APP-URL")
```
4. (Optional) Pass parameters to your app using `Launch("https://YOUR-STREAMLIT-APP-URL", { user: User().Email })` and read them in the app.

> Embedding arbitrary external sites **inside** a Canvas app screen isn't natively supported; use `Launch()` or a PCF iFrame control if required.
