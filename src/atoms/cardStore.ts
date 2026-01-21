import { atom, map } from "nanostores";

//TYPES
export type CartItem = {
  id: string;
  name: string;
  imageSrc: string;
  quantity: number;
  price: number;
};
type ItemDisplayInfo = Pick<CartItem, "id" | "name" | "imageSrc" | "price">;

//ATOMS
export const isCartOpen = atom(false);
export const cartItems = map<Record<string, CartItem>>({});

//FUNCTIONS
export function addCartItem({ id, name, imageSrc, price }: ItemDisplayInfo) {
  const existingEntry = cartItems.get()[id];
  if (existingEntry) {
    cartItems.setKey(id, {
      ...existingEntry,
      quantity: existingEntry.quantity + 1,
    });
  } else {
    cartItems.setKey(id, { id, name, imageSrc, price, quantity: 1 });
  }

  console.table(cartItems.get());
}

export function removeCartItem(id: string) {
  const items = { ...cartItems.get() };
  delete items[id];
  cartItems.set(items);
}

export function updateQuantity(id: string, quantity: number) {
  if (quantity <= 0) {
    removeCartItem(id);
  } else {
    const existingEntry = cartItems.get()[id];
    if (existingEntry) {
      cartItems.setKey(id, { ...existingEntry, quantity });
    }
  }
}

export function getCartTotal(): number {
  const items = Object.values(cartItems.get());
  return items.reduce((total, item) => total + item.price * item.quantity, 0);
}

export function getCartItemCount(): number {
  const items = Object.values(cartItems.get());
  return items.reduce((count, item) => count + item.quantity, 0);
}

export function clearCart(): void {
  cartItems.set({});
}
