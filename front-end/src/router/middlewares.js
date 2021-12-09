import { AuthService } from '@/services/auth.js'
// import cookie from 'vue-cookies'

export async function initCurrentUserStateMiddleware (to, from, next) {
  const currentUserId = localStorage.getItem("user")
  ? JSON.parse(localStorage.getItem("user")).id
  : null
  
  if (AuthService.hasRefreshToken() && !currentUserId) {
    try {
     /*  await AuthService.debounceRefreshTokens()
      await $store.dispatch('user/getCurrent') */
      next()
    } catch (e) {
      console.log(e)
    }
  } else {
    next()
  }  
}

export function checkAccessMiddleware (to, from, next) {
  const currentUserId = localStorage.getItem("user")
  // console.log("record => record.meta.role)",to.matched);
  const isAuthRoute = to.matched.some(record => record.meta.requiresAuth)
  const isAdminRoutes = to.matched.some(record => record.meta.isAdmin)
  const userRole = localStorage.getItem("user")
  ? JSON.parse(localStorage.getItem("user")).role
  : null

  if (isAuthRoute){
        if (currentUserId) {
          if(userRole !== "admin" && isAdminRoutes){
            alert("Access Denied")
              return next(to.matched[1].path); 
          }
          else {
            return next();
          }
        }
        else{
          return next("/login");
        }

  }
  const isGuestRoute = to.matched.some(record => record.meta.guest)
  if(isGuestRoute)
  {
    if (currentUserId) {
        return next("/home");
      }
      return next()
  }
  return next()
}

export function setPageTitleMiddleware (to, from, next) {
  const pageTitle = to.matched.find(record => record.meta.title)

  if (pageTitle) window.document.title = pageTitle.meta.title
  next()
}