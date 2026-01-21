import { atom, map } from "nanostores";

//TYPES
export type CartItem = {
  id: string;
  name: string;
  imageSrc: string;
  quantity: number;
};
type ItemDisplayInfo = Pick<CartItem, "id" | "name" | "imageSrc">;

//ATOMS
export const isCartOpen = atom(false);
export const cartItems = map<Record<string, CartItem>>({});

//FUNCTIONS
export function addCartItem({ id, name, imageSrc }: ItemDisplayInfo) {
  const existingEntry = cartItems.get()[id];
  if (existingEntry) {
    cartItems.setKey(id, {
      ...existingEntry,
      quantity: existingEntry.quantity + 1,
    });
  } else {
    cartItems.setKey(id, { id, name, imageSrc, quantity: 1 });
  }

  console.table(cartItems);
}
